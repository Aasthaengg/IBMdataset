n,m=[ord(i) for i in input().split()];n-=m;print(['<','>'][n>0] if n else'=')