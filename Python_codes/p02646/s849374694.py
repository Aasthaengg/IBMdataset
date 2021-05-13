A,a = map(int,input().split(" "))
B,b = map(int,input().split(" "))
c = int(input())
if abs(A-B) <= (a - b) * c:
    print("YES")
else:
    print("NO")