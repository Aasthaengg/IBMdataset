n=int(input())
lists=[]
for i in range(n):
    s=int(input())
    lists.append(s)
if all(lists[i]%2==0 for i in range(n)):
    print("second")
else:
    
    print("first")