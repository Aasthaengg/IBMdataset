n,a,b=map(int,input().split())

min_v=a*(n-1)+b
max_v=b*(n-1)+a

print(max(0,max_v-min_v+1))