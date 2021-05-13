ABC=list(map(int,input().split()))
for i in range(2):
    for j in range(i+1,3):
        if ABC[i]==ABC[j]:
            onaji=ABC[i]
            break
print(sum(ABC)-onaji*2)