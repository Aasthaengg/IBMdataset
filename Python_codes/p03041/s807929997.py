N,K = map (int, input ().split ())
a = input ()
if a[K-1] == 'A':
  print (a[:K-1]+'a'+a[K:])
elif a[K-1] == 'B':
  print (a[:K-1]+'b'+a[K:])
else:
  print (a[:K-1]+'c'+a[K:])