import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():
       s=input()
       for i in range(len(s)):
           for j in range(i+1,len(s)):
               if s[i]=='C' and s[j]=='F':
                   return 'Yes'
       return 'No'
    print(main())
resolve()