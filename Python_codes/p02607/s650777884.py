input()
print(len([i for n,i in enumerate(map(int,input().split()),1) if i%2==1 and n%2]))