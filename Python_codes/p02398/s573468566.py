a,b,c = list(map(int,input().split(" ")))
div = [i if(c%i==0)else 0 for i in range(a,b+1)]
div.append(0)
print(len(set(div))-1)