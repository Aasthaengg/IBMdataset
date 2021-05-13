def main():
  h,w = list(map(int,input().split()))
  s = [input() for i in range(h)]
  for i in range(0,h):
    for j in range(0,w):
      if s[i][j]=='#':
        print('#',end="")
      else:
        count=0
        for k in range(i-1,i+2):
          if k>=0 and k<h:
            for l in range(j-1,j+2):
              if l>=0 and l<w and s[k][l]=='#':
                count+=1
        print(count,end="")
    print()
    
main()