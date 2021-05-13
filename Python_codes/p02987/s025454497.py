def main():
 s = sorted(input())
 if s[0] == s[1] and s[3] == s[2] and s[1] != s[2]:
     print('Yes')
 else:
     print('No')
main()