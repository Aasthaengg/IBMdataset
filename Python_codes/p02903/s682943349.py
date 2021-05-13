def main():
  h,w,a,b=map(int,input().split())
  
  ans=[]
  ans+=["0"*a + "1"*(w-a) + "\n"]*b
  ans+=["1"*a + "0"*(w-a) + "\n"]*(h-b)
  print("".join(ans)[:-1])
  
if __name__=="__main__":
  main()