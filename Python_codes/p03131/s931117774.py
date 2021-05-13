K,A,B=map(int,input().split())

if B - A <= 2:
    print(K+1)
elif K <= A:
    print(K+1)
elif A % 2 == 1 and K % 2 == 1:
    print(B+(B-A)*((K-A-2)//2)+1)
elif A % 2 == 1 and K % 2 == 0:
    print(B+(B-A)*((K-A-1)//2))
elif A % 2 == 0 and K % 2 == 1:
    print(B+(B-A)*((K-A-1)//2))
else:
    print(B+(B-A)*((K-A-2)//2)+1)