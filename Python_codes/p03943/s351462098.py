a,b,c = (int(T) for T in input().split())
print(['No','Yes'][(a+b)==c or (b+c)==a or (c+a)==b])