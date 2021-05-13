from Queue import Queue
 
n, q = [ int( val ) for val in raw_input( ).split( " " ) ]
processes = Queue( )
for i in range( n ):
    name, time = raw_input( ).split( " " )
    processes.put( ( name, int( time ) ) )
  
qsum = 0
output = []
while not processes.empty( ):
    process = processes.get( )
    if process[1] <= q:
        qsum += process[1]
        output.append( "{:s} {:d}".format( process[0], qsum ) )
    else:
        processes.put( ( process[0], process[1]- q ) )
        qsum += q
 
print( "\n".join( output ) )