def f():
  ans,c=0,0
  for t in input().replace('BC','y'):
    if t=='y':ans+=c
    elif t=='A':c+=1
    else:c=0
  print(ans)
if __name__ == "__main__":f()