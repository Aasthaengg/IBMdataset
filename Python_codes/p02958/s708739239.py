n = int(input())
p = list(map(int, input().split()))

def bubble(input_list):
    cnt = 0
    flg = 0
    for i in range(len(input_list)):
        if i+1 != input_list[i]:
            cnt +=1
            flg = 1
    if flg == 1:
        return False, cnt
    else:
        return True, 0
a, b = bubble(p)

if b <= 2:
    print("YES")
else:
    print("NO")