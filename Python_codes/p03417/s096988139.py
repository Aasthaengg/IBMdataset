h,m=map(int,input().split());print((h-2)*(m-2)if h>=2 and m>=2 else 1 if h==m==1 else h+m-3)