a,b,c,d= map(int,input().split())
print('Yes' if -d<=c-a<=d or (-d<=b-a<=d and -d<=c-b<=d) else 'No')