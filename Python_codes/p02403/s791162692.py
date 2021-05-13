while 1:
    m,n=map(int, raw_input().split())
    if n==m==0: break
    else: print (('#'*n+'\n')*m)