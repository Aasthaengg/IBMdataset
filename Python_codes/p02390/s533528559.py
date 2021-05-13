r = int(input())

q1, r = divmod(r, 3600)
q2, r = divmod(r, 60)

print("{0}:{1}:{2}".format(q1, q2, r))