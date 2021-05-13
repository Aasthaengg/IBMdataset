
def myAnswer(A:int,B:int)-> str:
   if(A >B): return "GREATER"
   if(A<B): return "LESS"
   if(A==B): return "EQUAL"

def modelAnswer():
   tmp=1
def main():
   A = int(input())
   B = int(input())
   print(myAnswer(A,B))

if __name__ == '__main__':
   main()