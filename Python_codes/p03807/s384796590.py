N = int(input())
A = list(map(int, input().split()))
A_even = [num for num in A if num%2 == 0]
A_odd = [num for num in A if num%2 != 0]
e = len(A_even)
o = len(A_odd)

if(o%2 == 0):
    print("YES")
else:
    print("NO")