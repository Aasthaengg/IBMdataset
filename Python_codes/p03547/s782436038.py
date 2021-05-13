jisho ={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6}
x,y =input().split()
print(">" if jisho[x]>jisho[y] else "<" if jisho[x]<jisho[y] else "=")