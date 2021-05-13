def main():
 a,b,c = map(int,input().split())
 lim = a - b
 c -= min(c,lim)
 print(c)
main()