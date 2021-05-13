N = int(input())
x = input()

cnt_x = x.count("1")
px10 = 0
nx10 = 0
ans = [0] * (N+1)

for i in range(1, N+1): #Nまで先に出しておく
    popcnt = format(i,"b").count("1")
    fx = i % popcnt
    ans[i] = ans[fx] + 1

for i in range(N):
    px10 += (int(x[i]) * pow(2,N-1-i, cnt_x+1)) % (cnt_x+1)#0⇒1となった場合の合計
    if cnt_x != 0 and cnt_x != 1:
        nx10 += int(x[i])*pow(2,N-1-i,cnt_x-1) % (cnt_x-1)#1⇒0となった場合の合計
#print(px10)
#print(nx10)
for i in range(N):
    if x[i] == "0":
        xi10 = (px10+pow(2,N-1-i,cnt_x+1))%(cnt_x+1)
        print(ans[xi10]+1)
    else:
        if cnt_x != 1:
            xi10 = (nx10-pow(2,N-1-i,cnt_x-1))%(cnt_x-1)
            print(ans[xi10]+1)
        else:
            print(0)