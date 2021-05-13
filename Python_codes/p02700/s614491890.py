a,b,c,d = map(int, input().split())
word = ''
while True:
  c -= b
  if c <= 0:
    word = 'Yes'
    break
  a -= d
  if a <= 0:
    word = 'No'
    break
print(word)