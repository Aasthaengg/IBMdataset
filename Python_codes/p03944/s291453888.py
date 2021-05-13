w, h, n = map(int, input().split())
ans_list = [0,0,w,h]
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1 and ans_list[0]<x:
        ans_list[0] = x
    elif a == 2 and ans_list[2]>x:
        ans_list[2] = x
    elif a == 3 and ans_list[1]<y:
        ans_list[1] = y
    elif a == 4 and ans_list[3]>y:
        ans_list[3] = y
    ans = (ans_list[2]-ans_list[0])*(ans_list[3]-ans_list[1])
    if ans <= 0:
        print(0)
        exit()
print(ans)