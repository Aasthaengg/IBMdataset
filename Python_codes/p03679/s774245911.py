x,a,b=map(int,input().split())
print(('delicious',('safe','dangerous')[b-a>x])[a<b])