#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_D
#?????§????????????
#??????????????????????????????????????????????????\?????????????????¨??????
#???????????????????????????????????????????????????????????????????????????

cnt = 0
def insertion_sort(target_list,g):
    maxlen = len(target_list)
    global cnt
    for focus_index in range(g, maxlen):
        target = target_list[focus_index]
        
        if target < target_list[focus_index - g]:
            compare_index = focus_index - g

            while compare_index >= 0 and target_list[compare_index] > target:
                target_list[compare_index + g] = target_list[compare_index]
                compare_index = compare_index - g;
                cnt += 1
                
            target_list[compare_index + g] = target
    
    return target_list

def shell_sort(target_list):

    g = []
    g_value = 1
    while g_value <= len(target_list):
        g.append(g_value)
        g_value = 3 * g_value + 1
    g = g[::-1]
    
    print(len(g))
    print(*g)
    for i in range(0,len(g)):
        insertion_sort(target_list, g[i])

def main():
    n_list = int(input())
    target_list = [int(input()) for n in range(n_list)]
    cc = shell_sort(target_list)
    print(cnt)
    print("\n".join([str(n) for n in target_list]))
    
    
if __name__ == "__main__":
    main()