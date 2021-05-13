def myAnswer(A:int,B:int,C:int) -> int:
   l = sorted([A,B,C])
   red = l[2] // 2
   blue = l[2] // 2
   if(l[2] % 2 == 1):
      red += 1
   return abs(l[0]*l[1]*red - l[0]*l[1]*blue)
      

def modelAnswer():
   tmp=1
def main():
   A,B,C = map(int,input().split())
   print(myAnswer(A,B,C))
if __name__ == '__main__':
   main()