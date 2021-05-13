f = "{} {}\n".format
open(1, 'w').writelines([f(*sorted(map(int, line.split()))) for line in open(0).readlines()][:-1])
