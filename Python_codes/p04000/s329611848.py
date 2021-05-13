def main():
    h,w,n=map(int,input().split(' '))
    if n==0:
        print((h-2)*(w-2))
        for i in range(9):
            print(0)
        exit()
    draw_list=[]
    for i in range(n):
        draw=tuple(map(int,input().split(' ')))
        for j in range(3):
            for k in range(3):
                if 0<draw[0]-j<=h-2 and 0<draw[1]-k<=w-2:
                    draw_list.append((draw[0]-j,draw[1]-k))
    ans = [0]*9
    sorted_draw = sorted(draw_list)
    for n,i in enumerate(sorted_draw):
        if not n:
            ans_num=0
            tmp = i
            continue
        if tmp == i:
            ans_num+=1
        else:
            ans[ans_num] += 1
            tmp = i
            ans_num = 0
    ans[ans_num] += 1
    print((h-2)*(w-2)-sum(ans))
    for i in ans:
        print(i)



if __name__ == '__main__':
    main()
