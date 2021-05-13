n = int(input())
a = input().split()
a_odd  = []
a_even = []
for i in range(n):
    if (i+1)%2 == 0:
        a_even.append(a[i])
    else:
        a_odd.append(a[i])
        
if n%2 == 0:
    print(" ".join(a_even[::-1] + a_odd))
else:
    print(" ".join(a_odd[::-1] + a_even))