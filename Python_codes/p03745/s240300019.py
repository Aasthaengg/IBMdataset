#AGC013-A
n = int(input())
a = list(map(int,input().split()))
cnt = 0
first = True
up = False
down = False
for i in range(n):
    #print(i)
    if first:
        cnt += 1
        now = a[i]
        if i < n-1:
            #upのとき
            if a[i+1] > now:
                #print('up')
                up = True
                down = False
                first = False
            elif a[i+1] < now:
                #print('down')
                down = True
                up = False
                first = False
            else:
                #print("equal")
                up = False
                down = False
                first = True
                cnt -= 1

            
    else:
        now = a[i]
        if i < n-1:
            if up:
                if now > a[i+1]:
                    first = True

            elif down:
                if now < a[i+1]:
                    first = True

print(cnt)
