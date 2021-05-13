def myAnswer(N:int)->int:
   length = len(str(N))
   if(length == 1): return N
   l = list(str(N))
   tmp = 0
   for n in l[1:]:
      tmp += int(n)
   total = length * 9
   if(tmp == total - 9):
      return tmp + int(l[0])
   else:
      total += -9 + int(l[0]) - 1
      return total
def modelAnswer():
   tmp=1
def main():
   N = int(input())
   print(myAnswer(N))

if __name__ == '__main__':
   main()