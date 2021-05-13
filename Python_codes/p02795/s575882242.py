a,b,c=[int(input()) for i in range(3)]
def main(a,b,c):
    x=max([a,b])
    if c%x==0:
      print(int(c/x))
    else:
      print(int(c/x+1))
main(a,b,c)
