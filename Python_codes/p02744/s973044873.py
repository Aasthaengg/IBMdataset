N = int( input() )
alphabets = "abcdefghij"[ :N ]
types= ["a"]

for _ in range(N-1):
  for j in range(len(types)):
    target=types.pop(0)
    #print(set(target))
    for k in range(len(set(target))+1):
      types.append(target+alphabets[k])
    #print(types)
types.sort()
for each in types:
  print(each)