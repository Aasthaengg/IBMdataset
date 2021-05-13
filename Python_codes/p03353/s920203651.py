def main():
  s=input()
  k=int(input())
  l=len(s)
  
  substr=set()
  for alpha in 'abcdefghijklmnopqrstuvwxyz':
    for i in range(l):
      if s[i]==alpha:
        sub=s[i]
        substr.add(sub)
        j=i+1
        cnt=0
        while j<l and cnt<6:
          sub+=s[j]
          substr.add(sub)
          j+=1
          cnt+=1
    if len(substr)>k:
      break
      
  substr=list(substr)
  substr.sort()
  print(substr[k-1])
if __name__=='__main__':
  main()