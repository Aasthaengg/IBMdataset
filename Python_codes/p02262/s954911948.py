def insertionSort(insert_list, num, g): 
    cnt = 0 
    for i in range(g, num):
        temp = insert_list[i]
        j = i - g 
        while (j >= 0 and insert_list[j] > temp):
            insert_list[j+g] = insert_list[j]
            j -= g
            cnt += 1
        insert_list[j+g] = temp
    return insert_list, cnt 

def shellSort(shell_list, num):
    cnt = 0 
    G = [1] 
    G_num = 1 
    for i in range(num):
        G_num = G_num*3 + 1 
        if G_num > num:
            break
        else:
            G.append(G_num)
    G.reverse()
    m = len(G)

    for i in range(m):
        shell_list, cnt_num = insertionSort(shell_list, num, G[i])
        cnt += cnt_num
    return m, G, cnt, shell_list    

if __name__ == "__main__":
    num = int(raw_input())
    num_list = [int(raw_input()) for i in range(num)]

    m, G, cnt, shell_list = shellSort(num_list, num)

    print m
    G = map(str, G)
    print " ".join(G)
    print cnt 
    for i in shell_list:
        print i