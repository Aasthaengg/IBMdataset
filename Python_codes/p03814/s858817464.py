#B - A to Z String
s = input()

A = s.find('A')
Z = s.rfind('Z')

s_ans = s[A:Z+1]
print(len(s_ans))