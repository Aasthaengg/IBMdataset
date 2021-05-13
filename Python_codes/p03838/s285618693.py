def myAnswer(X:int,Y:int) -> int:
   result = []
   for i in range(2):
      tmpX = X
      ans = 0
      if(i==1):
         tmpX *= -1
         ans += 1
      for j in range(2):
         tmpY = Y
         if(j==1):
            tmpY *= -1
            ans += 1
         if(tmpX <= tmpY):
            result.append(ans + (tmpY - tmpX))
   return min(result)
def modelAnswer():
   return
def main():
   X,Y = map(int,input().split())
   print(myAnswer(X,Y))
if __name__ == '__main__':
   main()