x = int(input())
a = list(map(int, input().split()))

b = sorted(a, reverse=True)

ans_Alice = 0
ans_Bob = 0

for i in range(x): 
    if i%2 ==0:
        ans_Alice += int(b[i])
    else:
        ans_Bob += int(b[i])

        
print(int(ans_Alice) - int(ans_Bob))
