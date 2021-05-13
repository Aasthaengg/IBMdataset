a, b = map(int, raw_input().split())
c = float(a) / b

print str(a / b) + ' ' + str(a % b) + ' ' + str("{:.10f}".format(c))