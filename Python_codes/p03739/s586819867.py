
import sys
import copy
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = copy.copy(a)
sum_odd = sum(a[1::2])
sum_eve = sum(a[::2])

ans = 0
sum_a  = 0
for i in range(n):
        
    sum_a = sum_a + a[i]
        
    if sum_a *(-1)**(i+1) < 1:
        kari = 1-sum_a *(-1)**(i+1)
        a[i] += 1*(-1)**(i+1) *(kari)
        sum_a += 1*(-1)**(i+1) *(kari)
            
        ans = ans + abs(kari)
            
ans1 = 0
sum_b = 0
             
for i in range(n):
       
    sum_b = sum_b + b[i]
    if sum_b *(-1)**(i) < 1:
        kari = (1-sum_b *(-1)**(i))
        b[i] += 1*(-1)**(i) * kari
        sum_b += 1*(-1)**(i) * kari

        ans1 = ans1 + abs(kari)


print(min(ans,ans1))
