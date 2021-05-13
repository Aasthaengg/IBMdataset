a,b =map(int,input().split())
# b-aが、高さの差 2であれば左から1つめと2つめ nであればn-1つめとnつめ
n=b-a
print(int(0.5*n*(n+1)-b))