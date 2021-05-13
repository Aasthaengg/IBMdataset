ABC =list( map(int,input().split()))

if (ABC[0]%2==0) |(ABC[1]%2==0)|(ABC[2]%2==0):
    print(0)
else:
    ABC.sort()
    print(ABC[0]*ABC[1])