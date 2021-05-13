input()
print(len([j for i,j in enumerate(input().split()) if i%2==0 and int(j)%2]))