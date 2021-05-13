s = open(0).read().rstrip()

import re
m = re.search(r'A.*Z',s)

print(m.end() - m.start())