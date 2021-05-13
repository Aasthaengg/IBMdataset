N,K=map(int,input().split())
l=input().split()
numbers=[int(a) for a in l]
answers=sorted(numbers,reverse=True)
list=[]
for b in range(K):
    list.append(answers[b])
print(sum(list))
