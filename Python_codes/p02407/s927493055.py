n=int(input())
a=list(map(int,input().split()))
a.reverse()
string=""
count=0
for i in a:
    count+=1
    string+=str(i)
    if (count!=n):
        string+=" "

print(string)