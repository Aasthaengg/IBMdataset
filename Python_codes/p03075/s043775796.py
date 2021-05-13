def main():
 a = int(input())
 b = int(input())
 c = int(input())
 d = int(input())
 e = int(input())
 lim = int(input())
 if max(a,b,c,d,e) - min(a,b,c,d,e) <= lim:
     print('Yay!')
 else:
     print(':(')
main()