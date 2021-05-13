N=int(input())
A=list(map(int, input().split()))

flag=0 #増加で継続する場合1,減少で継続する場合-1,切り替わり時0
cnt=0

for i in range(N-1):
    if A[i+1]-A[i] >0:
        if flag ==1:
            continue
        elif flag ==-1:
            flag =0
            cnt+=1
        elif flag ==0:
            flag =1
    elif A[i+1]-A[i] <0:
        if flag ==-1:
            continue
        elif flag ==1:
            flag =0
            cnt+=1
        elif flag ==0:
            flag =-1
    elif A[i+1]-A[i] ==0:
        if flag == 0:
            flag = 0
        elif flag ==1:
            flag =1
        elif flag ==-1:
            flag =-1
print(cnt+1) #区切った数ではなく分割された個数なので+1