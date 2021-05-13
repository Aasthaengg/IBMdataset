[S,T]=list(map(str, input().split()))
[A,B]=list(map(int, input().split()))
U=str(input())
if U==S:
    print(A-1,B)
elif U==T:
    print(A,B-1)
