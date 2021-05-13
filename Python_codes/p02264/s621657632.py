#
# coding: utf-8

n, quantum = map(int, raw_input().split())

process_time = []
tim = 0

for x in xrange(n):
    pros, tt = raw_input().split()
    process_time.append([pros, int(tt)])

while True:
    if len(process_time) == 0: break
    pp = process_time.pop(0)
    if pp[1] > quantum :
        pp[1] = pp[1] - quantum
        process_time.append(pp)
        tim += quantum
    else:
        tim += pp[1]
        print pp[0] + " " +str(tim)